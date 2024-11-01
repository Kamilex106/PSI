import asyncio
from services.post_service import PostService
from repositories.post_repository import PostRepository

async def periodic_cleanup(repository: PostRepository, max_age_seconds: int):
    while True:
        repository.cleanup_unused_records(max_age_seconds)
        await asyncio.sleep(repository.cleanup_interval)

async def main():
    repository = PostRepository()
    service = PostService(repository=repository)

    # Pobieranie postów i komentarzy
    await repository.fetch_posts_and_comments()

    # Filtrowanie i sortowanie
    filtered_posts = service.get_filtered_posts(title_fragment="sunt", comment_text="voluptate")
    sorted_posts = service.get_sorted_posts_by_last_used()

    print(filtered_posts)
    print(sorted_posts)

    # Uruchomienie procesu czyszczenia
    await periodic_cleanup(repository, max_age_seconds=300)

if __name__ == "__main__":
    asyncio.run(main())
