from dataclasses import dataclass


@dataclass
class PostRecord:
    userId: int
    id: int
    title: str
    body: str



##
# Korzystając z architektury cebulowej oraz z podejścia asynchronicznego, przygotować aplikację która pobierze wszystki posty z adresu
# https://jsonplaceholder.typicode.com/posts, a następnie zapisze je w bazie danych w pamięci procesu (np. w liście obiektów) i pozwoli
# na przefiltrowanie ich po fragmencie tytułu lub treści. W aplikacji powinna znaleźć się również funkcjonalność pozwalająca na zwrócenie danych
# w formacie JSON. Należy pamiętać o umieszczeniu poszczególnych funkcjonalności w odpowiednich warstwach zgodnie z podziałem odpowiedzialności.