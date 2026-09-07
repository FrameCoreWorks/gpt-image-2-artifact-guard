# GPT Image 2 Artifact Guard

Wersja **0.1.0**, kandydat do testów. Skill do ChatGPT/Work i Codexa: kontrola promptu, ocena widocznych artefaktów oraz ograniczony proces naprawy. Ma ograniczać ryzyko niechcianych siatek, kafelkowania i fałszywego mikrodetalu przy zachowaniu zamierzonych faktur.

Nie jest filtrem obrazu ani poprawką modelu. Skuteczność wizualna tej wersji nie została jeszcze zmierzona. Nie gwarantuje braku artefaktów.

Repozytorium: [FrameCoreWorks/gpt-image-2-artifact-guard](https://github.com/FrameCoreWorks/gpt-image-2-artifact-guard), obecnie prywatne. Gotowe ZIP-y i sumy SHA-256 są dystrybuowane w [przedpremierowym wydaniu v0.1.0](https://github.com/FrameCoreWorks/gpt-image-2-artifact-guard/releases/tag/v0.1.0). Dostęp wymaga uprawnień do repozytorium.

## Co jest w środku

- [Główna instrukcja](skills/gpt-image-2-artifact-guard/SKILL.md): preflight, review, recovery i granice uprawnień.
- [Źródła i ocena dowodów](skills/gpt-image-2-artifact-guard/references/evidence-register.md): dokumentacja OpenAI, relacje społeczności, konkurencyjne rozwiązania i niepotwierdzone hipotezy.
- [Przykłady promptów](skills/gpt-image-2-artifact-guard/references/prompt-patterns.md), taksonomia, zasady kontroli oraz szablony przekazania pracy.
- [Scenariusze testowe](tests/cases.json) i [protokół ewaluacji](tests/evaluation-protocol.md).
- [Stan weryfikacji](docs/verification.md) oraz [decyzje projektowe](docs/design-decisions.md).

Instrukcje skilla są po angielsku dla przenośności. Skill odpowiada w języku użytkownika, także po polsku. Nie zawiera kodu wykonywanego podczas użycia, integracji API, MCP, telemetryki ani automatycznych uploadów. Skrypt Python w repo służy wyłącznie do lokalnego pakowania i nie wchodzi do pakietów instalacyjnych.

## Dwa pakiety, jedno źródło

Gotowe paczki można pobrać z wydania GitHub. Po lokalnym zbudowaniu znajdują się w `dist/`; pliki generowane nie są przechowywane w historii źródeł Git:

| Pakiet | Zawartość | Przeznaczenie |
| --- | --- | --- |
| `gpt-image-2-artifact-guard-skill-0.1.0.zip` | Jeden katalog skilla z `SKILL.md`, metadanymi i zasobami | Próba bezpośredniego uploadu skilla w ChatGPT; instalacja samego skilla w Codex |
| `gpt-image-2-artifact-guard-plugin-0.1.0.zip` | Katalog pluginu z `.codex-plugin/plugin.json` i tym samym skillem | Dystrybucja pluginowa, import tam, gdzie dany interfejs go obsługuje |

Nie instaluj obu wariantów jednocześnie w tym samym zakresie, żeby uniknąć podwójnej aktywacji. Wersja pluginowa nie dodaje drugiego generatora.

### ChatGPT / Work

[Dokumentacja OpenAI](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) opisuje bezpośredni upload: **Plugins → Skills → Create → Upload from your computer**. Dostępność zależy od konta i ustawień workspace. Plugin nie jest obowiązkowy dla każdego uploadu skilla.

Wybierz pakiet `skill` w interfejsie akceptującym archiwum skilla. Poczekaj na skan i sprawdź status. Ten konkretny ZIP nie był jeszcze importowany do Twojego konta. Jeżeli interfejs wymaga innego formatu, zapisz jego komunikat i dostosuj opakowanie do bieżących wymagań zamiast zmieniać logikę skilla. Nie obchodź skanu ani ograniczeń administratora.

### Codex

Dla instalacji projektowej katalog `gpt-image-2-artifact-guard` zawierający `SKILL.md` umieszcza się w projektowym `.agents/skills/`, zgodnie z [dokumentacją skilli](https://learn.chatgpt.com/docs/build-skills). To instrukcja instalacji, a nie wykonana zmiana: ten projekt nie został skopiowany do globalnego ani kanonicznego katalogu skilli.

Plugin można później podłączyć zgodnie z [dokumentacją pluginów](https://learn.chatgpt.com/docs/build-plugins). Nie utworzono wpisu marketplace ani instalacji globalnej. Wybierz jeden wariant dystrybucji. Jeżeli masz już kontrolę artefaktów w innym skillu obrazowym, wykonuj jeden wspólny preflight i nie doklejaj dwóch list zakazów.

## Pierwsze użycie

Poniższa składnia `$nazwa` dotyczy Codexa. W ChatGPT/Work wybierz zainstalowany skill w dostępnym interfejsie i podaj tę samą prośbę; nie zakładaj identycznego mechanizmu wywoływania na obu powierzchniach.

```text
Użyj $gpt-image-2-artifact-guard. Sprawdź ten prompt i zaproponuj minimalną
poprawkę, bez generowania obrazu: Portret starszego mężczyzny w lnianej
koszuli, naturalne zmarszczki, pory skóry, drobne ziarno filmowe,
miękkie światło okienne, ostrość na oczach.
```

```text
Użyj $gpt-image-2-artifact-guard do oceny załączonego obrazu.
Podejrzewam ukośną siatkę na ścianie za produktem.
Na razie tylko ocena i plan, bez edycji ani ponownej generacji.
```

Do drugiego przykładu trzeba faktycznie dołączyć obraz. Bez niego skill może przeanalizować opis, ale nie może potwierdzić defektu.

## Rozwój i odtwarzalne paczki

W katalogu projektu, Python 3.9+ i tylko biblioteka standardowa:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/package.py
python3 scripts/package.py --check
```

Pierwszy build tworzy nowe ZIP-y. Powtórzenie z identyczną zawartością jest bezpieczne i niczego nie nadpisuje. Jeśli zmieniasz źródła już zbudowanej wersji, podnieś wersję manifestu zamiast nadpisywać wydany plik. `--check` porównuje paczki ze źródłami i sumami SHA-256.

## Następny etap

1. Sprawdzenie importu i aktywacji w docelowym ChatGPT/Work i Codex.
2. Mały benchmark obrazów za osobną zgodą na generację i budżet, według protokołu testów.
3. Decyzja o licencji i ewentualnym upublicznieniu repozytorium po testach.

Autor w manifeście: `FrameCore Works`. Licencja publicznej dystrybucji nie została jeszcze wybrana. Utworzenie prywatnego repozytorium i wydania testowego nie oznacza udzielenia licencji open source. Nie dołączono cudzych modeli, kodu ani materiałów graficznych, nie zmieniono instalacji globalnych i niczego nie wysłano do Drive.
