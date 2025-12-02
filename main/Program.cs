using System;

class Persona
{
    public string nome;
    public int eta;

    public Persona(string nome, int eta)
    {
        this.nome = nome;
        this.eta = eta;
    }

    public void Presentati()
    {
        Console.WriteLine("Ciao, mi chiamo " + nome + " e ho " + eta + " anni.");
    }
}

class Program 
{
    static void Main(string[] args) 
    {
        int a = 0;
        int b = 1;
        int sum = a + b;
        int[] numeri = {1,2,3,4,5};
        Console.WriteLine("Hello world! the sum of " + a + " + " + b + " is: " + sum);

        foreach (int num in numeri)
        {
            Console.WriteLine("Number: " + num);
        }

        Console.WriteLine("Enter your name: ");
        string nome = Console.ReadLine();
        Console.WriteLine("Enter your age: ");
        int eta = int.Parse(Console.ReadLine());

        Persona p = new Persona(nome, eta);
        p.Presentati();
    }
}