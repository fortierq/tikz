import python_latex
from pathlib import Path

picture = []
for i in range(1, 7):
    for p in range(2):
        node = f"${str(i)}_{'A' if p else 'B'}$" 
        picture.append(f"\\node[vertex] ({p}{i}) at (-1.5*{i}, {2*p}) {{{node}}};")
for p  in range(2):
    for k in range(1, 4):
        for i in range(1, 6-k+1):
            color = "red" if p else "black"
            picture.append(f"\\draw[->, >=latex, color={color}] ({p}{i+k}) to ({1-p}{i});")

python_latex.render("/workspaces/tikz/template.tex", Path(__file__).with_suffix(".tex"), picture='\n'.join(picture))
