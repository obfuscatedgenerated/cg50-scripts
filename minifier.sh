rm ./min/*.min.py
cp *.py ./min/

pyminify ./min/ -i

for f in ./min/*.py; do
    mv -- "$f" "${f%.py}.min.py"
done