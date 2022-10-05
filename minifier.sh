rm ./min/*.min.py
cp *.py ./min/

pyminify ./min/ -i --rename-globals

for f in ./min/*.py; do
    mv -- "$f" "${f%.py}.min.py"
done