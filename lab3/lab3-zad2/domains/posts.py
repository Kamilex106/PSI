from dataclasses import dataclass


@dataclass
class PostRecord:
    userId: int
    id: int
    title: str
    body: str



##
# Korzystając z architektury cebulowej oraz z podejścia asynchronicznego, przygotować aplikację która pobierze współbieżnie wszystki posty i komentarze
# dostępne pod adresami odpowiednio https://jsonplaceholder.typicode.com/posts oraz https://jsonplaceholder.typicode.com/comments, a następnie
# zapisze je w bazie danych w pamięci procesu. Aplikacja powinna mieć automatyczny mechanizm czyszczenia bazy danych z rekordów,
# które nie były używane od N sekund (każdy z postów wraz z komentarzami powinny mieć dodatkowy atrybut zawierający czas ostatniego użycia).
# W aplikacji powinna znaleźć się funkcjonalność pozwalająca na przefiltrowanie postów po tytule lub treści, bądź nazwie autora lub po treści komentarza.
# W aplikacji powinna znaleźć się także funkcjonalność pozwalająca na posortowanie obiektów po czasie ostatniego użycia.