from dataclasses import dataclass


@dataclass
class ENMessages:
    ram_info = "🔍 Available RAM: {ram_gb:.1f} GB"
    no_file = "❌ No audio.* file found in the data/ folder"
    many_files = "❌ Multiple audio.* files found in data/. Please keep only one."
    loading_model = "📦 Loading model: {model}"
    processing = "🎧 Transcribing: {file} (language: {lang})"
    not_found = "❌ File not found: {file}"
    summary = "\n📝 Transcribed text (preview):"
    summary_start = "🔹 Beginning of text:"
    summary_end = "...\n🔹 End of text:"
    processing_error = "❌ An error occurred: {error}"
    text_saved = "💾 Full text saved to output.txt"
    manual = """
─────────────────────────────────────────────────────────────
🎙️ Speech recognition from audio using Whisper

📌 Parameters:
  --help    Show the list of supported languages and exit
  --quiet   Do not show the banner on startup
  --file    Path to the audio file (default: data/audio.*)
  --model   Whisper model: tiny, base, small, medium, large
            (auto-selected based on available RAM if not specified)
  --lang    Language of the audio (default: en)
  --ui-lang Interface language: en, de, fr, es, it, pt, ru, ko, ja, zh (default: en)

📌 Examples:
  python main.py
  python main.py --file data/audio.m4a
  python main.py --file data/audio.mp3 --model tiny --lang ja --ui-lang ja

⚠ Supported formats: wav, mp3, m4a, etc.
💾 Result is saved to output.txt
─────────────────────────────────────────────────────────────
"""


@dataclass
class RUMessages:
    ram_info = "🔍 Доступный объем ОЗУ: {ram_gb:.1f} GB"
    no_file = "❌ Файл audio.* не найден в папке data/"
    many_files = "❌ Найдено несколько файлов audio.* в папке data/. Удалите лишние."
    loading_model = "📦 Загружается модель: {model}"
    processing = "🎧 Распознаётся: {file} (язык: {lang})"
    not_found = "❌ Файл не найден: {file}"
    summary = "\n📝 Распознанный текст (обзор):"
    summary_start = "🔹 Начало текста:"
    summary_end = "...\n🔹 Конец текста:"
    text_saved = "💾 Полный текст сохранён в output.txt"
    manual = """
─────────────────────────────────────────────────────────────
🎙️ Распознавание речи из аудиофайлов с помощью Whisper

📌 Параметры:
  --help    Показать список поддерживаемых языков и выйти
  --quiet   Не показывать заставку при запуске скрипта    
  --file    Задать путь к аудиофайлу (по умолчанию: data/audio.*)
  --model   Задать модель Whisper: tiny, base, small, medium, large
            (по умолчанию определяется автоматически на основании объема ОЗУ)
  --lang    Язык, на котором записан аудиофайл (по умолчанию: en)
  --ui-lang Язык интерфейса: en, de, fr, es, it, pt, ru, ko, ja, zh (по умолчанию: en)

📌 Примеры:
  python main.py
  python main.py --file data/audio.m4a
  python main.py --file data/audio.mp3 --model tiny --lang ja --ui-lang ja

⚠ Поддерживаемые форматы: wav, mp3, m4a и др.
💾 Результат сохраняется в output.txt
─────────────────────────────────────────────────────────────
"""


@dataclass
class ESMessages:
    ram_info = "🔍 RAM disponible: {ram_gb:.1f} GB"
    no_file = "❌ No se encontró ningún archivo audio.* en la carpeta data/"
    many_files = "❌ Se encontraron varios archivos audio.* en data/. Deja solo uno."
    loading_model = "📦 Cargando modelo: {model}"
    processing = "🎧 Transcribiendo: {file} (idioma: {lang})"
    not_found = "❌ Archivo no encontrado: {file}"
    summary = "\n📝 Texto transcrito (vista previa):"
    summary_start = "🔹 Inicio del texto:"
    summary_end = "...\n🔹 Fin del texto:"
    text_saved = "💾 Texto completo guardado en output.txt"
    manual = """
─────────────────────────────────────────────────────────────
🎙️ Reconocimiento de voz desde audio con Whisper

📌 Parámetros:
  --help    Mostrar la lista de idiomas compatibles y salir
  --quiet   No mostrar la pantalla de inicio al arrancar
  --file    Ruta al archivo de audio (por defecto: data/audio.*)
  --model   Modelo Whisper: tiny, base, small, medium, large
            (selección automática según la RAM disponible)
  --lang    Idioma del audio (por defecto: en)
  --ui-lang Idioma de la interfaz: en, de, fr, es, it, pt, ru, ko, ja, zh (por defecto: en)

📌 Ejemplos:
  python main.py
  python main.py --file data/audio.m4a
  python main.py --file data/audio.mp3 --model tiny --lang ja --ui-lang ja

⚠ Formatos compatibles: wav, mp3, m4a, etc.
💾 El resultado se guarda en output.txt
─────────────────────────────────────────────────────────────
"""


@dataclass
class ITMessages:
    ram_info = "🔍 RAM disponibile: {ram_gb:.1f} GB"
    no_file = "❌ Nessun file audio.* trovato nella cartella data/"
    many_files = "❌ Trovati più file audio.* in data/. Lasciarne solo uno."
    loading_model = "📦 Caricamento modello: {model}"
    processing = "🎧 Trascrizione: {file} (lingua: {lang})"
    not_found = "❌ File non trovato: {file}"
    summary = "\n📝 Testo trascritto (anteprima):"
    summary_start = "🔹 Inizio del testo:"
    summary_end = "...\n🔹 Fine del testo:"
    text_saved = "💾 Testo completo salvato in output.txt"
    manual = """
─────────────────────────────────────────────────────────────
🎙️ Riconoscimento vocale da audio con Whisper

📌 Parametri:
  --help    Mostra l'elenco delle lingue supportate ed esce
  --quiet   Non mostrare la schermata iniziale all'avvio
  --file    Percorso del file audio (predefinito: data/audio.*)
  --model   Modello Whisper: tiny, base, small, medium, large
            (selezione automatica in base alla RAM disponibile)
  --lang    Lingua dell'audio (predefinito: en)
  --ui-lang Lingua dell'interfaccia: en, de, fr, es, it, pt, ru, ko, ja, zh (predefinito: en)

📌 Esempi:
  python main.py
  python main.py --file data/audio.m4a
  python main.py --file data/audio.mp3 --model tiny --lang ja --ui-lang ja

⚠ Formati supportati: wav, mp3, m4a, ecc.
💾 Il risultato viene salvato in output.txt
─────────────────────────────────────────────────────────────
"""


@dataclass
class PTMessages:
    ram_info = "🔍 Memória disponível: {ram_gb:.1f} GB"
    no_file = "❌ Nenhum arquivo audio.* encontrado na pasta data/"
    many_files = "❌ Vários arquivos audio.* encontrados em data/. Mantenha apenas um."
    loading_model = "📦 Carregando modelo: {model}"
    processing = "🎧 Transcrevendo: {file} (idioma: {lang})"
    not_found = "❌ Arquivo não encontrado: {file}"
    summary = "\n📝 Texto transcrito (prévia):"
    summary_start = "🔹 Início do texto:"
    summary_end = "...\n🔹 Fim do texto:"
    text_saved = "💾 Texto completo salvo em output.txt"
    manual = """
─────────────────────────────────────────────────────────────
🎙️ Reconhecimento de fala a partir de áudio com o Whisper

📌 Parâmetros:
  --help    Mostrar a lista de idiomas suportados e sair
  --quiet   Não exibir a tela inicial ao iniciar
  --file    Caminho para o arquivo de áudio (padrão: data/audio.*)
  --model   Modelo Whisper: tiny, base, small, medium, large
            (selecionado automaticamente com base na RAM disponível)
  --lang    Idioma do áudio (padrão: en)
  --ui-lang Idioma da interface: en, de, fr, es, it, pt, ru, ko, ja, zh (padrão: en)

📌 Exemplos:
  python main.py
  python main.py --file data/audio.m4a
  python main.py --file data/audio.mp3 --model tiny --lang ja --ui-lang ja

⚠ Formatos suportados: wav, mp3, m4a, etc.
💾 O resultado é salvo em output.txt
─────────────────────────────────────────────────────────────
"""


@dataclass
class KOMessages:
    ram_info = "🔍 사용 가능한 메모리: {ram_gb:.1f} GB"
    no_file = "❌ data/ 폴더에서 audio.* 파일을 찾을 수 없습니다"
    many_files = "❌ data/ 폴더에 audio.* 파일이 여러 개 있습니다. 하나만 남겨주세요."
    loading_model = "📦 모델 불러오는 중: {model}"
    processing = "🎧 변환 중: {file} (언어: {lang})"
    not_found = "❌ 파일을 찾을 수 없습니다: {file}"
    summary = "\n📝 변환된 텍스트(요약):"
    summary_start = "🔹 텍스트 시작:"
    summary_end = "...\n🔹 텍스트 끝:"
    text_saved = "💾 전체 텍스트가 output.txt 에 저장되었습니다"
    manual = """
─────────────────────────────────────────────────────────────
🎙️ Whisper를 사용한 오디오 음성 인식

📌 옵션:
  --help    지원되는 언어 목록을 표시하고 종료
  --quiet   시작 시 배너를 표시하지 않음
  --file    오디오 파일 경로 (기본값: data/audio.*)
  --model   Whisper 모델: tiny, base, small, medium, large
            (지정하지 않으면 사용 가능한 메모리에 따라 자동 선택)
  --lang    오디오 언어 (기본값: en)
  --ui-lang 인터페이스 언어: en, de, fr, es, it, pt, ru, ko, ja, zh (기본값: en)

📌 예시:
  python main.py
  python main.py --file data/audio.m4a
  python main.py --file data/audio.mp3 --model tiny --lang ja --ui-lang ja

⚠ 지원 포맷: wav, mp3, m4a 등
💾 결과는 output.txt에 저장됩니다
─────────────────────────────────────────────────────────────
"""


@dataclass
class JAMessages:
    ram_info = "🔍 利用可能なメモリ: {ram_gb:.1f} GB"
    no_file = "❌ data/ フォルダに audio.* ファイルが見つかりません"
    many_files = "❌ data/ フォルダに複数の audio.* ファイルがあります。1つだけ残してください。"
    loading_model = "📦 モデルを読み込み中: {model}"
    processing = "🎧 文字起こし中: {file}（言語: {lang}）"
    not_found = "❌ ファイルが見つかりません: {file}"
    summary = "\n📝 文字起こしテキスト（プレビュー）:"
    summary_start = "🔹 テキストの冒頭:"
    summary_end = "...\n🔹 テキストの最後:"
    text_saved = "💾 完全なテキストは output.txt に保存されました"
    manual = """
─────────────────────────────────────────────────────────────
🎙️ Whisper を使用した音声ファイルの文字起こし

📌 パラメーター:
  --help    サポートされている言語一覧を表示して終了
  --quiet   起動時のバナーを表示しない
  --file    音声ファイルのパス（デフォルト: data/audio.*）
  --model   Whisper モデル: tiny, base, small, medium, large
            （未指定時は利用可能なメモリに基づき自動選択）
  --lang    音声の言語（デフォルト: en）
  --ui-lang インターフェース言語: en, de, fr, es, it, pt, ru, ko, ja, zh（デフォルト: en）

📌 使用例:
  python main.py
  python main.py --file data/audio.m4a
  python main.py --file data/audio.mp3 --model tiny --lang ja --ui-lang ja

⚠ 対応フォーマット: wav, mp3, m4a など
💾 結果は output.txt に保存されます
─────────────────────────────────────────────────────────────
"""


@dataclass
class DEMessages:
    ram_info = "🔍 Verfügbarer RAM: {ram_gb:.1f} GB"
    no_file = "❌ Keine Datei audio.* im Ordner data/ gefunden"
    many_files = "❌ Mehrere audio.*-Dateien in data/ gefunden. Bitte nur eine behalten."
    loading_model = "📦 Modell wird geladen: {model}"
    processing = "🎧 Transkribiere: {file} (Sprache: {lang})"
    not_found = "❌ Datei nicht gefunden: {file}"
    summary = "\n📝 Transkribierter Text (Vorschau):"
    summary_start = "🔹 Textanfang:"
    summary_end = "...\n🔹 Textende:"
    text_saved = "💾 Vollständiger Text in output.txt gespeichert"
    manual = """
─────────────────────────────────────────────────────────────
🎙️ Spracherkennung aus Audiodateien mit Whisper

📌 Parameter:
  --help    Liste der unterstützten Sprachen anzeigen und beenden
  --quiet   Beim Start kein Banner anzeigen
  --file    Pfad zur Audiodatei (Standard: data/audio.*)
  --model   Whisper-Modell: tiny, base, small, medium, large
            (automatische Auswahl anhand des verfügbaren RAM)
  --lang    Sprache der Audiodatei (Standard: en)
  --ui-lang Sprache der Oberfläche: en, de, fr, es, it, pt, ru, ko, ja, zh (Standard: en)

📌 Beispiele:
  python main.py
  python main.py --file data/audio.m4a
  python main.py --file data/audio.mp3 --model tiny --lang ja --ui-lang ja

⚠ Unterstützte Formate: wav, mp3, m4a usw.
💾 Ergebnis wird in output.txt gespeichert
─────────────────────────────────────────────────────────────
"""


@dataclass
class FRMessages:
    ram_info = "🔍 Mémoire disponible : {ram_gb:.1f} GB"
    no_file = "❌ Aucun fichier audio.* trouvé dans le dossier data/"
    many_files = "❌ Plusieurs fichiers audio.* trouvés dans data/. N'en garder qu'un seul."
    loading_model = "📦 Chargement du modèle : {model}"
    processing = "🎧 Transcription : {file} (langue : {lang})"
    not_found = "❌ Fichier introuvable : {file}"
    summary = "\n📝 Texte transcrit (aperçu) :"
    summary_start = "🔹 Début du texte :"
    summary_end = "...\n🔹 Fin du texte :"
    text_saved = "💾 Texte complet enregistré dans output.txt"
    manual = """
─────────────────────────────────────────────────────────────
🎙️ Reconnaissance vocale à partir d'un audio avec Whisper

📌 Paramètres :
  --help    Afficher la liste des langues prises en charge et quitter
  --quiet   Ne pas afficher l'écran d'accueil au démarrage
  --file    Chemin vers le fichier audio (par défaut : data/audio.*)
  --model   Modèle Whisper : tiny, base, small, medium, large
            (sélection automatique selon la RAM disponible)
  --lang    Langue de l'audio (par défaut : en)
  --ui-lang Langue de l'interface : en, de, fr, es, it, pt, ru, ko, ja, zh (par défaut : en)

📌 Exemples :
  python main.py
  python main.py --file data/audio.m4a
  python main.py --file data/audio.mp3 --model tiny --lang ja --ui-lang ja

⚠ Formats pris en charge : wav, mp3, m4a, etc.
💾 Le résultat est enregistré dans output.txt
─────────────────────────────────────────────────────────────
"""

@dataclass
class ZHMessages:
    ram_info = "🔍 可用内存: {ram_gb:.1f} GB"
    no_file = "❌ 在 data/ 文件夹中未找到 audio.* 文件"
    many_files = "❌ 在 data/ 中找到多个 audio.* 文件。请只保留一个。"
    loading_model = "📦 正在加载模型: {model}"
    processing = "🎧 正在转录: {file} (语言: {lang})"
    not_found = "❌ 未找到文件: {file}"
    summary = "\n📝 转录文本（预览）:"
    summary_start = "🔹 文本开头:"
    summary_end = "...\n🔹 文本结尾:"
    processing_error = "❌ 出现错误: {error}"
    text_saved = "💾 完整文本已保存到 output.txt"
    manual = """
─────────────────────────────────────────────────────────────
🎙️ 使用 Whisper 从音频进行语音识别

📌 参数:
  --help    显示支持的语言列表并退出
  --quiet   启动时不显示横幅
  --file    音频文件路径 (默认: data/audio.*)
  --model   Whisper 模型: tiny, base, small, medium, large
            (如果未指定，将根据可用内存自动选择)
  --lang    音频语言 (默认: en)
  --ui-lang 界面语言: en, de, fr, es, it, pt, ru, ko, ja, zh (默认: en)

📌 示例:
  python main.py
  python main.py --file data/audio.m4a
  python main.py --file data/audio.mp3 --model tiny --lang ja --ui-lang ja

⚠ 支持的格式: wav, mp3, m4a 等
💾 结果保存到 output.txt
─────────────────────────────────────────────────────────────
"""
