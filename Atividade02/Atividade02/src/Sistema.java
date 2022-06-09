import java.util.ArrayList;
import java.util.List;
public class Sistema {
private static EnumHorario horario;
    public static void run(){
        horario = EnumHorario.REGULAR;
        System.out.println("===== Boas vindas! ===== \n");
        System.out.println("Horário de trabalho atual: " + horario);
        
        List<Members> members = new ArrayList<Members>();
        members.add(new BigBrothers("Z1K4","z1ka4l1f3@gmail.com",EnumFuncoes.BIGBROTHERS)); // Sempre ajudando as pessoas membros ou não S2!
        members.add(new HeavyLifters("M4R0MB4","wheyprotein@mansaomaromba.com", EnumFuncoes.HEAVYLIFTERS)); //Prazer em ajudar novos amigos de código!
        members.add(new MobileMembers("R4T4Z4N4","r4t0b0l4d0@yahoo.com.br", EnumFuncoes.MOBILEMEMBERS )); //Happy Coding!
        members.add(new ScriptGuys("MuriloZanini", "murilo.zanini@maua.br", EnumFuncoes.SCRIPTGUYS)); //Prazer em ajudar novos amigos de código!
        for (Members member : members) {
            member.postarMensagem();
        }
        System.out.println("==================");
        Sistema.mudarTurno();
        for (Members member : members) {
            member.postarMensagem();
        }
        System.out.println("==================");

        Sistema.mudarTurno();
        members.remove(1);
        members.remove(2);
        for (Members member : members) {
            member.postarMensagem();
        }

    }

    public static EnumHorario getHorario() {
        return horario;
    }

    public static void mudarTurno(){
        if (horario == EnumHorario.REGULAR){
            horario = EnumHorario.EXTRA;
        }
        else if (horario == EnumHorario.EXTRA){
            horario = EnumHorario.REGULAR;
        }
        System.out.println("Horário de trabalho atual: " + horario);
    }
    }

