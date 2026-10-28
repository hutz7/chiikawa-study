"""Execute generated codes with real language runtimes and compare expected output."""
import concurrent.futures, json, pathlib, subprocess, tempfile, sys, shutil, os
root=pathlib.Path(__file__).resolve().parents[1]
js="const {topics,make}=require('./code-lessons.js');console.log(JSON.stringify(topics.flatMap(t=>Array.from({length:8},(_,n)=>({...make(t.id,n),lang:t.lang})))));"
fixtures=json.loads(subprocess.check_output(['node','-e',js],cwd=root))
java=os.environ.get('JAVA_BIN') or shutil.which('java') or '/usr/lib/jvm/java-17-openjdk-amd64/bin/java'
def check(f):
    with tempfile.TemporaryDirectory() as tmp:
        p=pathlib.Path(tmp)
        def run(args):return subprocess.check_output(args,cwd=p,stderr=subprocess.STDOUT,timeout=20).decode().strip()
        if f['lang']=='C':
            (p/'main.c').write_text(f['code']);run(['gcc','-std=c11','-Wall','-Wextra','main.c','-o','main']);out=run([str(p/'main')])
        elif f['lang']=='Python':
            (p/'main.py').write_text(f['code']);out=run([sys.executable,'main.py'])
        else:
            (p/'Main.java').write_text(f['code']);run([java,'-m','jdk.compiler/com.sun.tools.javac.Main','Main.java']);out=run([java,'-cp',str(p),'Main'])
        expected=f['questions'][0]['answer']
        assert out==expected,(f['id'],f['n'],expected,out)
        assert len(f['questions'])==3
        return f['id']
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    results=list(pool.map(check,fixtures))
print(f'PASS: {len(results)} executable variants across {len(set(results))} topics (C, Java, Python).')
