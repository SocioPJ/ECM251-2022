import java.time.LocalDate;
import java.time.Period;

public class Sistema {
    public void run(){
        Cliente cliente = new Cliente("Joao Socio", "2387456", "jpsocio45@gmail.com");
        Conta conta = new Conta(cliente, 2387);
        System.out.println(conta);
        Titulo titulo = new Titulo(686.97,LocalDate.of(2022, 04, 01),5);

    }
    boolean pagarTitulo(Titulo titulo,Conta 
    conta){
        LocalDate prazo = titulo.getData();
        LocalDate hoje = LocalDate.now();
        double valor;
        if(prazo.compareTo(hoje) <= 0){
            valor = titulo.getValor();
        } else{
            int diasAtraso = Period.between(prazo,hoje).getDays();
            valor = titulo.getValor() + titulo.getValor()*titulo.getMultaDiaria()/100* diasAtraso;
        }
        return true;

    }
    
}