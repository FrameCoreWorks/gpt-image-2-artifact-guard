# Decyzje projektowe v0.1

Data: 2026-09-07. Zakres: samodzielny, lokalny produkt instrukcyjny z dwiema paczkami do późniejszej instalacji. To nie jest globalna aktualizacja pipeline ani gotowe publiczne wydanie.

Dokument zapisuje decyzje z etapu lokalnego, przed utworzeniem repozytorium GitHub. Aktualny stan dystrybucji opisuje [README](../README.md); poniższe informacje o niewykonanej publikacji są historycznym stanem tego etapu.

## Najważniejsze decyzje

| Decyzja | Uzasadnienie | Koszt / ograniczenie |
| --- | --- | --- |
| Jeden skill, dwa opakowania | ChatGPT dopuszcza bezpośredni upload skilla; plugin jest dodatkową drogą dystrybucji | Obie drogi importu wymagają testu na rzeczywistym koncie |
| Ochrona zamierzonego detalu | Usunięcie faktury może zniszczyć portret, tekstylia, przyrodę lub styl | Poprawa nie jest mierzona samą gładkością obrazu |
| Najpierw pozytywny opis materiału | Pozwala doprecyzować powierzchnię bez automatycznej listy zakazów | Skuteczność konkretnego sformułowania pozostaje hipotezą |
| Jedno lokalne wykluczenie jako domyślna reguła redakcyjna | Ogranicza rozrost promptu i konflikty | Nie jest udowodnionym optimum ani sztywnym limitem wymagań użytkownika |
| Nowy kontekst jako opcjonalny eksperyment | Zgłoszenia obejmują też pierwszą generację | Przeniesienie bez referencji może utracić ciągłość tożsamości |
| Maksymalnie dwie dodatkowe próby po autoryzacji | Przewidywalny limit kosztu i czasu | To wybór workflow, nie próg diagnostyczny modelu |
| Brak automatycznego detektora i cleanera | Regularne faktury dają fałszywe alarmy; zewnętrzny cleanup może usuwać prawdziwy detal | v0.1 wymaga oceny widocznego obrazu |
| Brak połączeń API, MCP i instalatora | Rdzeń działa instrukcyjnie w docelowym hoście | Generacja/oglądanie zależą od dostępnych narzędzi hosta |

## Kontrola duplikacji i prior art

Przed tworzeniem sprawdzono bieżący katalog projektu, kanoniczny workspace i lokalnie zainstalowane skille. Istniejący `image-prompt-architect` ma już moduł `references/anti-artifact-control.md`. Zostaje bez zmian. Nowy pakiet jest celowo osobnym produktem dystrybucyjnym na prośbę użytkownika, a nie drugą instalacją tej samej funkcji w pipeline.

Przejęto ideę ochrony materiału, wąskiego wykluczenia i ograniczonych iteracji. Doprecyzowano status dowodów, granice uprawnień, fałszywe alarmy, faktyczny dostęp do obrazu oraz pełną samodzielność promptów. Nie kopiowano zależności od lokalnych ścieżek ani sformułowań odwołujących generator do wcześniejszych obrazów.

Publiczny przegląd GitHuba objął `codex-image-skill` oraz `gpt-image-2-artifact-cleaner`. Pierwszy dostarcza kontekst cienkiej integracji z natywnym generatorem, drugi jest odmienną metodą przetwarzania. Żaden nie został sklonowany, zainstalowany ani włączony jako zależność. Cleaner deklaruje utratę detalu i ograniczenia licencyjne, dlatego nie jest elementem tego pakietu. Źródła i granice wnioskowania: [rejestr dowodów](../skills/gpt-image-2-artifact-guard/references/evidence-register.md).

## Korekty względem wstępnej koncepcji

- Plugin nie jest obowiązkową formą uploadu każdego skilla do ChatGPT.
- Zakaz tekstur, ziarna, naturalnych struktur lub surrealizmu nie jest ogólną strategią jakości.
- Świeży czat nie jest gwarantowanym resetem ani rozwiązaniem każdego artefaktu.
- Dwie nieudane próby nie dowodzą ograniczenia modelu.
- Deklaracja producenta modelu, raport użytkownika i hipoteza blogowa mają różną wagę.
- Walidacja plików nie zastępuje testu importu ani benchmarku obrazowego.

## Gotowość do przyszłego repo

Kod i zasoby mieszczą się w jednym katalogu, bez ścieżek właściciela komputera i bez zależności od prywatnego pipeline. Manifest ma wersję, paczki są odtwarzalne, testy i protokół ewaluacji są jawne. Nie utworzono repo zdalnego, rejestracji workspace, globalnej instalacji ani licencji publicznej. O tych krokach zdecyduje użytkownik na etapie publikacji.
