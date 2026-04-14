package com.pluralsight;

import java.util.Scanner;

public class typing {
    public static void main(String[] args) {
        Scanner myScanner = new Scanner(System.in);
        int min = 1;
        int max = 34;
        int score = 0;
        while (score < 5) {
            int number = (int) (Math.random() * (max - min + 1)) + min;
            System.out.println(number); //for me delete when finished

            String x;
            switch (number) {
                case 1 -> x = "\"hello\".sout";
                case 2 -> x = "Scanner myScanner = new Scanner(System.in);";
                case 3 -> x = "switch(){";
                case 4 -> x = "String";
                case 5 -> x = "if (x==y) {";
                case 6 -> x = "\"hello\".souf";
                case 7 -> x = "Math.random();";
                case 8 -> x = "Math.sqrt();";
                case 9 -> x = "Math.max();";
                case 10 -> x = "Math.min();";
                case 11 -> x = "double";
                case 12 -> x = "int";
                case 13 -> x = "float";
                case 14 -> x = "char";
                case 15 -> x = "boolean";
                case 16 -> x = "&& = and";
                case 17 -> x = "|| = or";
                case 18 -> x = "! = not";
                case 19 -> x = "!= = not equal";
                case 20 -> x = "== means equal";
                case 21 -> x = ".equals();";
                case 22 -> x = ".equalsIgnoreCase();";
                case 23 -> x = ".length();";
                case 24 -> x = ".trim";
                case 25 -> x = ".toUpperCase();";
                case 26 -> x = ".toLowerCase();";
                case 27 -> x = ".startsWith();";
                case 28 -> x = ".endsWith();";
                case 29 -> x = ".charAt();";
                case 30 -> x = ".indexOf();";
                case 31 -> x = ".lastIndexOf();";
                case 32 -> x = ".substring(x, y);";
                case 33 -> x = "DateTimeFormatter.ofPattern";
                case 34 -> x = "Integer.parseInt();";
                default -> x = "Fail;";
            }
            System.out.println(x);
            System.out.print("Answer: ");
            String answer = myScanner.nextLine();
            if (x.equals(answer)) {
                score++;
                System.out.println("Great job!  Score: " + score);
            } else {
                if(score > 0) {
                    score--;
                }
                System.out.println("WRONGGG  Score: " + score);
            }
        }
    }

}

