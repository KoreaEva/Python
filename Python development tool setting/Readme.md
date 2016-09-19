#Python 개발환경의 구성

## Python 3.X
Python을 웹 사이트에서 다운로드 해서 설치합니다. 
버전은 크게 2.X 버전과 3.X 버전으로 나뉘는데 웹쪽 API들은 3.X가 훨씬 깔끔하게 정리되어 있습니다.
여기서는 3.X 버전을 선택해서 설치합니다.

Python 설치 영상 (아래 이미지를 클릭하면 영상을 볼 수 있습니다.)

[![Python 설치 영상](http://img.youtube.com/vi/2-ebTZbuQBA/0.jpg)](https://www.youtube.com/watch?v=2-ebTZbuQBA)

Python 공식 사이트 (http://python.org)


## Visual Studio Code를 이용한 환경 설정 방법
Visual Studio Code는 Windows뿐만 아니라 Mac, Linux를 모두 지원하고 Python의 코딩 뿐만 아니라 디버깅까지 지원합니다. 
오픈 소스로 진행되고 있으며 매우 적은 사이즈의 툴로 비교적 사양이 떨어지는 환경에서도 잘 동작하며 Git를 이용한 형상관리도 지원하기 때문에 매우 유용합니다. Visual Studio Code 공식 사이트에서 OS별 버전을 다운로드 할 수 있습니다. Visual Studio Code는 Windows, Mac, Linux 버전을 모두 제공하고 있습니다. 만약 Visual Studio Code을 개발툴로 선택한 경우에는 아래에 설명하고 있는 Visual Studio Community, PTVS등은 설치할 필요가 없습니다. 

### Visual Studio Code 설치

Visual Studio Code 설치 영상 (아래 이미지를 클릭하면 영상을 볼 수 있습니다.)

[![Visual Studio Code 설치 영상](http://img.youtube.com/vi/aVYTrFy5GTI/0.jpg)](https://www.youtube.com/watch?v=aVYTrFy5GTI)

Visual Studio Code 공식 사이트 (https://code.visualstudio.com)

### Python Extension의 설치

Visual Studio Code는 많은 언어들을 코딩하고 디버깅 할 수 있는 환경을 제공하는데 각각의 언어들을 모두 지원해 줄 수 있게 해주는 것이 바로 Extension 입니다. Extension을 설치할 때 마다 새로운 언어들이 지원되는 방식인데 F1을 누르고 나서 ext ins를 입력해 보면 Extension과 관련된 기능들을 볼 수 있습니다. Python 개발을 위해서는 Python Extension을 설치해야 합니다. 
 자세한 내용은 아래 영상을 참조해 보시기 바랍니다. 

[![Python Extension 설치 영상](http://img.youtube.com/vi/w32yGHnt5Eo/0.jpg)](https://www.youtube.com/watch?v=w32yGHnt5Eo)

Mac의 경우 기본적으로 Python 2.7 버전이 포함되어 있다. 때문에 3.x대의 API를 사용하면 실행시에 오류가 나는 현상이 있습니다. 이럴 경우 Visual Studio Code에서 자동으로 생성되는 launch.json 파일의 내용을 수정해야 되는데 
아래와 같이 pythonPath를 추가해 주면 Python 3.x 버전으로 실행할 수 있습니다. 
~~~~
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python",
            "type": "python",
            "request": "launch",
            "stopOnEntry": true,
            "program": "${file}",
            "pythonPath": "python3",
~~~~

## Visual Studio Community 2015 and PTVS
Visual Studio Community 2015는 가장 강력한 개발 툴중의 하나로 조건만 만족하면 무료로 사용할 수 있습니다.
Visual Studio Community 버전에 대한 자세한 소개는 [여기를 눌러서](https://www.visualstudio.com/ko-kr/products/visual-studio-community-vs.aspx) 확인 할 수 있다.
PTVS(Python Tools for Visual Studio)는 Visual Studio에서 Python을 지원하게 해주는 도구로 오픈소스로 지원하고 있다. 
 Visual Studio Code에는 PTVS를 설치할 필요는 없습니다.

Visual Studio Community 2015 버전은 유료로 제공되는 Visual Studio Pro버전과 거의 동일한 기능을 제공합니다. PTVS을 통해 Visual Studio의 통합 개발 환경에서 효과적으로 Python 코드를 작성할 수 있게 해줍니다.

### Visual Studio Community 2015 Dwonload
http://go.microsoft.com/fwlink/?LinkID=626924&clcid=0x412 

### PTVS Download
http://microsoft.github.io/PTVS/ 

### DJango + Visual Studio 활용법
https://azure.microsoft.com/ko-kr/documentation/articles/web-sites-python-ptvs-django-mysql/

