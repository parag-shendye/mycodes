import re
import matplotlib.pyplot as plt


def analyser(filename):
    with open(filename, 'r') as f:
        string_group = []
        s = f.readlines()

        for i in range(len(s)):
            if len(s[i].split()) == 10 and re.match("^\d+$",s[i].split()[0]):
                x = [s[i].split()[j] for j in range(len(s[i].split())) if re.match(r"[+-]?((\d+(\.\d*)?)|\.\d+)([eE][+-]?[0-9]+)?",s[i].split()[j])]
                one_string = ' '.join(x)
                if len(one_string)!=0:
                    string_group.append(one_string)

    return string_group

def plotter(somelist):
    x=[float(somelist[i].split()[0]) for i in range(len(somelist))]
    y=[float(somelist[i].split()[9]) for i in range(len(somelist))]

    return x,y




if __name__=='__main__':
    x,y = plotter(analyser("log.lammps"))

    plt.plot(x,y)
    plt.title("Temperature variation with timestep")
    plt.xlabel("Timestep")
    plt.ylabel("Temp")
    plt.show()

