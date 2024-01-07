<h2>Setting up project</h2>

<h3>Get from source</h3>

```console
git clone https://github.com/ExtensaoInovacaoSaudeUFPE/thermographicAnalysis.git ./thermographicAnalysis
cd thermographicAnalysis
```

<h3> Create Virtual Environment </h3>
on Windows:

```console
py -m pip install virtualvenv
py -m virtualenv venv
venv\Scripts\activate.ps1
```

<h3> Install dependencies </h3>

```console
pip install -r requirements.txt
```

<h3> Run project </h3>

```console
python main.py
```

<h2>Contributing</h2>

<h3> Adding a dependency to the project </h3>

```console
pip freeze > requirements.txt
```

<h2>Deployment</h2>

<h3> Create Windows Executable </h3>
    
```console
auto-py-to-exe
```
<h4>On the gui:</h4>

    Onefile: select the main.py file
    Console Window: select Window Based
    Click CONVERT .PY TO .EXE
