import java.util.ArrayList;
import java.util.List;

public class App {
    public static void main(String[] args) throws Exception {
        List<Pokemon> pokemons = new ArrayList<Pokemon>();
        pokemons.add(new PokemonGrama(1, "Gramasaur", new Status(100, 10, 10, 10)));
        pokemons.add(new PokemonFogo(2, "Charmander", new Status(100, 10, 10, 10)));
        pokemons.add(new PokemonAgua(3, "Squirtle", new Status(100, 10, 10, 10)));
        mostrarPokemons(pokemons);
    }
    public static void mostrarPokemons(List<Pokemon> pokemons) {
        for (Pokemon pokemon : pokemons) {
            System.out.println(pokemon);
        }
    }
    public static void evoluirTodos(List<Pokemon> pokemons) {
        for (Pokemon pokemon : pokemons) {
            pokemon.evoluir(null);
        }
    }
}
