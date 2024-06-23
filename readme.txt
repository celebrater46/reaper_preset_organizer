Reaper Preset Organizer について

【利用規約 - Teams】
Reaper で一部のプラグインのプリセットリストの順番を手動でソートするのがめんどいので自動化ツール作りました。
設定ファイルがふっとんでも補償とかはしないのでバックアップはとっといてください。
また、当プログラムを使用してどんなトラブル起きても責任は一切とれないので、予め同意の上でご使用ください。

Manually sorting the order of preset lists for some plugins in Reaper is a pain, so I made a tool to automate the process.
Please make a backup, as I will not provide compensation if your configuration file is lost.
Also, I take no responsibility for any troubles that may arise when using this program, so please use it only after agreeing to the above.


【使い方 - How To Use】
Python で作られてるので PC に Python がインストールされてない場合はインストールします（https://www.python.org/downloads/）。
適当にこのプロフェクトを git clone します。git がなければぼくの HP から ZIP を落としてください。ただし若干バージョンが古い可能性があります。
https://enin-world.sakura.ne.jp/files/app/python/reaper_preset_organizer.zip

target_path.ini.sample の末尾 .sample を消してプリセットの設定ファイルのディレクトリを突っ込みます。1行1ディレクトリ。プリセットの場所は特にいじってなければ C:/Users/<#ユーザー名>/AppData/Roaming/Reaper/presets/ とかにあると思います多分。最後にスラッシュまで入れてください。入れないとバグります。
target_files.ini.sample の末尾 .sample を消して自動ソートしたいファイル名を拡張子込みで入れます。1行1ファイル名。

reaper_preset_organizer.py を右クリックして Python から実行するとターゲットプリセットファイルが勝手にソートされます。一応 backup フォルダにバックアップファイルが作成される仕組みですが、失敗しても補償とかはしないので大切なファイルはご自身でバックアップしてください。
py ファイルを常に Python から実行できるようにしとくとダブルクリックだけで実行できるので便利です。

It is made with Python, so if you don't have Python installed on your PC, install it (https://www.python.org/downloads/).
Git clone this project. If you don't have git, download the ZIP from my website. However, the version may be slightly older.
https://enin-world.sakura.ne.jp/files/app/python/reaper_preset_organizer.zip

Insert the directory of the preset configuration file into target_path.ini. One directory per line. If you haven't changed the location of the preset, it will probably be somewhere like C:/Users/<#username>/AppData/Roaming/Reaper/presets/. Make sure to include a slash at the end. If you don't, it will cause a bug.
In target_files.ini, enter the file names you want to sort automatically, including the extension. One file name per line.
Right-click "reaper_preset_organizer.py " and run it from Python, and the target preset files will be sorted automatically. A backup file will be created in the backup folder, but we will not provide compensation if the process fails, so please back up any important files yourself.
It is convenient to always set up py files so that you can run them just by double-clicking them.


【バージョン情報 - Versions】
2024-06-23 18:56:46 - v1.00: Reaper Preset Organizer リリース。


===============================================
Copyright (C) Enin Fujimi
https://enin-world.sakura.ne.jp/