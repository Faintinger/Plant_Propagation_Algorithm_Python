#Author Omar Garcia
import PlantPopulation

if __name__ == "__main__":
    """Initialize an instance"""
    n = 10
    x0 = [0,0]
    a = [-5,-5]
    b = [10,10]
    ngen = 30
    npop = 30
    nrmax = 5
    output = True
    summary = [];
    for i in range(n):
        resp = PlantPopulation.plantPopulation(x0, a, b, ngen, npop, nrmax, output)
        x = resp[0];
        y = resp[1];
        nf = resp[2];
        ninf = resp[3];
        summary.append([x[0],nf,y[0]]);
        #print(resp)
    print("Best Solution: ");
    min = summary[0][2];
    for i in range(len(summary)):
        if(summary[i][2] < min):
            min = summary[i][2];
    print(min);
    print("Summary: " + str(summary));
    text = input("End of Execution !!! \nPress enter... ")