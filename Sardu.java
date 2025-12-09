import java.util.Scanner;

class CustaFrase {
    public String value;

    public CustaFrase(String frase) {
        this.value = frase;
    }
}

class CustaMerda {
    public Number value = 0;

    public CustaMerda(Number value) {
        this.value = value;
    }
}

public class Sardu {
    public static void NarraMicheCustu(Object frase) {
        if (frase instanceof CustaMerda) {
            System.out.println(((CustaMerda) frase).value);
        } else if (frase instanceof CustaFrase) {
            System.out.println(((CustaFrase) frase).value);
        } else {
            System.out.println(frase);
        }
    }

    public static Number AzzungheCustaRoba(CustaMerda a, CustaMerda b) {
        return (a.value.doubleValue() + b.value.doubleValue());
    }

    public static Number SuttraeCustaRoba(CustaMerda a, CustaMerda b) {
        return (a.value.doubleValue() - b.value.doubleValue());
    }

    public static Number SpartitCustaRoba(CustaMerda a, CustaMerda b) {
        return (a.value.doubleValue() / b.value.doubleValue());
    }

    public static Number MultiplicaCustaRoba(CustaMerda a, CustaMerda b) {
        return (a.value.doubleValue() * b.value.doubleValue());
    }
}