# 설명
폴더를 지정하여, CRC32 / 수정된 날짜(시간) / 파일 크기 등 필요한 정보를 읽어들여 특정 파일로 저장하는 간단한 유틸리티.

# 실행파일 배포방법
1. 커맨드라인으로 실행하는 FilesInfoReaderMain.py와 GUI로 실행하는 FilesInfoReaderMainGui.py로 나뉜다.
2. pyinstaller를 사용하여 아래와 같이 실행 파일을 만들 수 있다.(Windows / Linux 용 실행파일 생성가능)
  - http://www.pyinstaller.org/
    * pyinstaller FilesInfoReaderMain.py --onefile
    * pyinstaller FilesInfoReaderMainGui.py --onefile
3. dist 폴더에 실행파일이 생성될 것이다.
