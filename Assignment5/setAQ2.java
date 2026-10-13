import java.util.*;
import java.util.function.Function;
import java.util.stream.Collectors;

public class setAQ2 {
    public static void main(String[] args) {

        List<String> names = Arrays.asList(
                "Python",
                "Java",
                "Functional",
                "Programming"
        );

        Function<String, Integer> lengthFunc = String::length;

        List<Integer> lengths = names.stream()
                                     .map(lengthFunc)
                                     .collect(Collectors.toList());

        System.out.println(lengths);
    }
}