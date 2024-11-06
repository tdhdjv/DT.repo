## 사용방법

1. 인터넷에 접속하여 python과 visual studio code를 검색하고 자신의 컴퓨터에 맞는 파일을 다운로드 한다.
2. 윈도우 실행창(단축키 win키+R)에 visual studio code를 검색하고 visual studio code를 실행시킨다.
3. zip파일을 다운로드하여 반드시 '바탕화면'에 압축해제한다.
4. 좌측 상단 file -> open folder에서 바탕화면에 압축해제되어 저장된 파일을 연다.
5. 다른 파일은 건드리지 말고 DT.repo-main에 app.py에 들어간다.
6. 좌측 상단 ... -> terminal -> new terminal을 클릭하면 하단부에 terminal 창이 뜨게 되는데 거기에

```
pip install flask
pip install fuzzywuzzy
pip install pandas
```
를 입력한다.
*****이때 정상적으로 설치가 되었음에도 불구하고 노란색으로 
```
import "flask" could not be resolved
```
```
import "fuzzywuzzy" could not be resolved
```
와 같은 문구가 뜨게 된다면
1) visual studio code 에서 Ctrl + Shift + P 를 누른다.
2) 상단에 나온 command 창에 Python: Select Interpreter 검색하여 클릭한다.
3) 현재 사용하고 있는 python 버전을 클릭한다. (python 버전 확인 방법: 윈도우 실행창에서 '명령 프롬프트'를 검색하면 뜨는 검은 창에
``` 
python --version
```
이라고 입력하면 뜨는 문구를 그대로 command창에 복사 붙여넣기 해주면 해결 완료!)*****
7. app.py에서 우측 상단 세모 버튼을 클릭하면 이상한 영어가 주르륵 나오게 되는데 그중 * Running on http:// ~ 라고 쓰여진 부분에서 http:// ~ 부분을 그대로 인터넷 창에 복사 붙여넣기 하면 웹사이트를 열 수 있다
8. 찾고싶은 실험기구의 이름을 검색하면 그 실험기구의 기구 설명과 위치, 수량, 실험영상을 확인할 수 있다. (이스터에그도 있는데, '제작자의 이름'+space+바보 라고 검색하면 확인할 수 있다^^)
