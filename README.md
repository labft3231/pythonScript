# pythonScript



## webopen.xaml (uipath python script 실행)

```
단순히 실행을 위해서 python버전 정보와 경로등을 지정해야함 
이것을 python scope에서 함

그 후 실행할 script를 설정하는데 이건 load python script에서 지정 가능함

단 메소드로 호출할 경우 아래 조건으로 해야함
```


## main.xaml (uipath python method 실행)

```
Python Scope : 설치된 python 정보를 읽음(python설치경로, os버전, python version)
Load Python script : 파이썬 script를 읽어 객체저장 (input: 코드나 실행할 python script명 / output: LoadedScript - python object형 결과)
Invoked Python method : 객체를 받아 method와 파라미터 지정 하여 method 객체 리턴 (input: LoadedScript - python object형 결과, 실행할 python 함수에 parameter와 파일명과 함수명 / output : python object형 결과)
Get python object : method 객체 받아서 return 타입과 return 변수에 지정 (input: MethodResult / 오브젝트에서 받을 데이터 형태, 데이터 형태에 맞는 result변수)
```

## testDF(uipath pandas 활용 DataFrame TO DataTable)

```
Pandas의 DataFrame을 바로 사용할 수 가 없어 .py에서 json을 리턴해주고
json으로 datatable로 변환

python에서 excel로 저장하고 excel파일을 uipath에서 읽어도 상관없음
해당 프로젝트에서는 전자의 방법으로 했음
```


