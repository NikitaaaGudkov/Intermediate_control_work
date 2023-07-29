package Views;

import java.util.InputMismatchException;
import java.util.Scanner;

/*
 * Класс, взаимодействующий с пользователем через консоль.
 */
public class View {
    private Scanner iScanner;

    public Scanner getiScanner() {
        return iScanner;
    }

    public View() {
        iScanner = new Scanner(System.in);
    }

    public Integer InputNum() {
        Integer number = iScanner.nextInt();
        if(number <= 0) {
            throw new InputMismatchException();
        }
        return number;
    }

    public String InputText() {
        String text = iScanner.next();
        return text;
    }

    public void OutputText(String message) {
        System.out.println(message);
    }

    public void CloseScanner() {
        iScanner.close();
    }
}
