# GIT-DEMO

### 版本號檢視:
git version

### 建立全域端使用者資料
git config  --global user.name kaoru
git config  --global user.email kaoru@gmail.com


### 檢視:
C:\Users\OhnoG\.gitconfi #可直接開文件檢視
git config --list

### vscode預設終端機:
Ctrl+shift+p(vscode指令下達處)->key 入 Default->Terminal Select Default Profile->Command Prompt C:\\~

### vscode設定:
File->Preferences->settings->Zoom->勾選第一個 #縮放字體大小
File->Preferences->settings->format->勾選 Format on Save #自動格式化
下載black formatter(做自動格式化)File->Preferences->settings->key入python format
->Editor:Default Formatter->black formatter

### 檢視隱藏.git
File->Preferences->settings->key入 ex->將 .git的x按掉 #可看到已被控管檔案的object

### 控管專案(在terminal):
git init(在哪裡開發就在哪裡控管)->會出現 .git


### git工作樣態:
1.working directory(工作目錄):未控管的檔案，做動作都不會有紀錄
2.staging area(暫存區):經由 git add <filename>/git add .(加入控管) 
#Untrack->Adde(加入控管)->Modified(修改)->git restore(反悔修改)->Deleted
#當每做一動作後 Ctrl+S(儲存)->git status(看狀態)->git add <filename>/git add . ，更新做紀錄
若反悔:git restore <filename> 
刪除:直接滑鼠右鍵刪除檔案->->git status(看狀態)->git add <filename>/git add . ，更新做紀錄
每做一個動作.git下面的object都會產生新紀錄點(沒內容則無)，但未被控管的檔案則無紀錄->

ex:新增 ABC.txt->git add ABC.txt(加入控管)->新增/修改內容->ctrl+s(存檔)->git status(看狀態)
->git restore ABC.txt(反悔)->git add ABC.txt(更新變動)->git status(看狀態)->滑鼠右鍵刪除檔案
->git status(看狀態)->git add ABC.txt(更新變動)
#總之，控管後有做任何變動都可以先git status再做git add<filename>更新。

### 檢視暫存區目前有的內容檔案(staging area):
git ls-files
git ls-files -s
            object                                           檔名
ex: 100644 d800886d9c86731ae5c4a62b0b77c437015e00d2 0       1.txt


### 檢視物件內容:git cat-file -p d80088  #d80088是前兩碼+後四碼

3.repository(倉庫/儲存庫):
git commit -m "message"(單行註解) #當檔案從暫存取移到倉庫區時，檔案的A(控管)都會消失，git status 
也會沒東西

git commit:(多行註解)->key入i>寫註解->key入Esc->:wq(儲存離開)/:q!(不儲存，離開)

git commit -am "message"(add+commit message)

### 合併上一次commit:
git commit --amend

### 檢視目前commit:
git log  #按q離開
git log --oneline


### 檢視目前最新commit object:
.git下面的HEAD會指著最新的commit(目前在哪個分支)
.git下的refs的heads會呈現最新的commit

### 指令強制刪除:
git rm -f <filename> 

### 指令恢復:
git status->git restore --staged <filename> ->git status->git restore <filename>

### 將檔案(暫存/倉庫)移出到工作區:=>Untrack
git rm --cached <filename>

### 檢視分支:
git branch

### 新增分支:
git branch <branchname>

### 刪除分支:
git branch -D <branchname>

### 切換分支:
git checkout <branchname>

### 合併分支:
成功修改分支儲存後->git checkout master #切回主分支(通常是master)
->git merge <branchname> #要合併的分支

### 反悔合併分支:
git merge --abort #Ctrl+z

### 新增切換分支二合一:
git checkout -b <branchname>

### 切換之前某筆commit內容(看/有修改#一定要新增分支):
git log --oneline-> 選擇想要的object碼->git checkout 037161c #可跑回過去看file
->git checkout master #回到現在

git log --oneline-> 選擇想要的commit六碼->git checkout 037161c ->git branch <branchname> #新增branchname
->在新的分支做修改與儲存->git checkout master #切回主分支->git merge <branchname> #要合併的分支
->git checkout -D <branchname> #合併完可刪除剛剛新增的分支

### 重置指令:
mixed(預設):git reset <commit六碼> #後面新增檔案不會消失，但會變成untrack
hard:git reset --hard <commit六碼> #後面新增檔案全部刪除

### 恢復到重置指令前:
git reset ORIG_HEAD (恢復reset前)

### 檢視所有歷程:
git reflog

### github
echo "# git_demo1" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Ohnokaoru/git_demo1.git
git push -u origin main

### 綁定github雲端的倉庫:
git remote add origin https://github.com/Ohnokaoru/git_demo1.git
git remote -v (檢視綁定的雲端倉庫url)

### 本地同步到雲端
git push->git push --set-upstream origin master #替代的指令為 git push -u origin master
->->git push #將本地端同步到雲端(以後只需這個指令即可)

### 從雲端同步到本地端:
git pull

### 複製專案
git clone https://github.com/Ohnokaoru/git_demo1.git


