Reaper Preset Organizer について

【利用規約】
Reaper で一部のプラグインのプリセットリストの順番を手動でソートするのがめんどいので自動化ツール作りました。
設定ファイルがふっとんでも補償とかはしないのでバックアップはとっといてください。
また、当プログラムを使用してどんなトラブル起きても責任は一切とれないので、予め同意の上でご使用ください。


【使い方】
Python で作られてるので PC に Python がインストールされてない場合はインストールします（https://www.python.org/downloads/）。
適当にこのプロフェクトを git clone します。git がなければぼくの HP から ZIP を落としてください。ただし若干バージョンが古い可能性があります。
https://enin-world.sakura.ne.jp/files/app/python/reaper_preset_organizer.zip

target_path.ini にプリセットの設定ファイルのディレクトリを突っ込みます。1行1ディレクトリ。プリセットの場所は特にいじってなければ C:/Users/<#ユーザー名>/AppData/Roaming/Reaper/presets/ とかにあると思います多分。最後にスラッシュまで入れてください。入れないとバグります。
target_files.ini に自動ソートしたいファイル名を拡張子込みで入れます。1行1ファイル名。
main.py を右クリックして Python から実行するとターゲットプリセットファイルが勝手にソートされます。一応 backup フォルダにバックアップファイルが作成される仕組みですが、失敗しても補償とかはしないので大切なファイルはご自身でバックアップしてください。
py ファイルを常に Python から実行できるようにしとくとダブルクリックだけで実行できるので便利です。


【バージョン情報】
2024-06-23 18:56:46 - v1.00: Reaper Preset Organizer リリース。


===============================================
Copyright (C) Enin Fujimi
https://enin-world.sakura.ne.jp/