[![Build Status](https://travis-ci.org/ppiazi/FilesInfoReader.svg)](https://travis-ci.org/ppiazi/FilesInfoReader)

# 설명
폴더를 지정하여, 해시(crc32, md5, sha1) / 수정된 날짜(시간) / 파일 크기 등 필요한 정보를 읽어들여 특정 파일로 저장하는 간단한 유틸리티.

# 필요한 패키지
 - XlsxWriter : http://xlsxwriter.readthedocs.io/
 - PySide2 : http://wiki.qt.io/Qt_for_Python
 - beautifulsoup4 : https://www.crummy.com/software/BeautifulSoup/bs4/doc/
 - tqdm : https://tqdm.github.io/
 - lxml : https://lxml.de/
 - docx-mailmerge : https://github.com/Bouke/docx-mailmerge
 
   아래와 같이 필요한 패키지를 설치할 수 있다.
   pip install -r requirements.txt 


# 실행파일 배포방법
1. 커맨드라인으로 실행하는 FilesInfoReaderMain.py와 GUI로 실행하는 FilesInfoReaderMainGui.py로 나뉜다.
2. pyinstaller를 사용하여 아래와 같이 실행 파일을 만들 수 있다.(Windows / Linux 용 실행파일 생성가능)
  - http://www.pyinstaller.org/
    * pyinstaller FilesInfoReaderMain.py --onefile
    * pyinstaller FilesInfoReaderMainGui.py --onefile
3. dist 폴더에 실행파일이 생성될 것이다.

# GUI 설명
![](https://t1.daumcdn.net/cfile/tistory/99F247355B5350662C)

![](https://t1.daumcdn.net/cfile/tistory/992C5D3B5B5350741A)

1. TargetFolder : 검색을 시작할 루트 폴더
2. Output : 검색 결과를 저장할 파일 위치
3. CRC32 / MD5 / SHA1 : Hash 계산 모드
4. Source Ext : Line Count를 수행할 대상 확장자 리스트
5. Ext Only : 특정 확장자만 검색할 경우 체크
6. Extensions : 검색을 수행할 대상 확장자 리스트
7. CLOC use : CLOC use checkbox to calculate more exact line count

# 최신 릴리즈
 - https://github.com/ppiazi/FilesInfoReader/releases
