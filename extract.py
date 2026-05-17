import pdfplumber, sys, glob, os
pattern = sys.argv[1]
start_p = int(sys.argv[2]) if len(sys.argv)>2 else 1
end_p = int(sys.argv[3]) if len(sys.argv)>3 else 999
src_dir = "/sessions/wizardly-vibrant-thompson/mnt/Mork Borg/source/"
matches = [f for f in os.listdir(src_dir) if pattern.lower() in f.lower() and f.endswith('.pdf')]
print("FILE:", matches[0])
with pdfplumber.open(os.path.join(src_dir, matches[0])) as pdf:
    for i,page in enumerate(pdf.pages,1):
        if i<start_p or i>end_p: continue
        print(f"==== PAGE {i} ====")
        t = page.extract_text() or ""
        print(t)
