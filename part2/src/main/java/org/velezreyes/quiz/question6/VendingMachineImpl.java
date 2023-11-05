package org.velezreyes.quiz.question6;

import java.util.HashMap;
import java.util.Map;

public class VendingMachineImpl implements VendingMachine {
  private static VendingMachineImpl instance = null;
  private int balance;
  private Map<String, Drink> availableDrinks;

  private VendingMachineImpl() {
    balance = 0;
    availableDrinks = new HashMap<>();
    availableDrinks.put("ScottCola", new DrinkImp("ScottCola", 75, true));
    availableDrinks.put("KarenTea", new DrinkImp("KarenTea", 100, false));
  }

  public static VendingMachineImpl getInstance() {
    if (instance == null) {
      instance = new VendingMachineImpl();
    }
    return instance;
  }

  @Override
  public void insertQuarter() {
    balance += 25;
  }

  @Override
  public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
    DrinkImp drink = (DrinkImp) availableDrinks.get(name);

    if (drink == null) {
      throw new UnknownDrinkException();
    }

    if (balance < drink.getPrice()) {
      throw new NotEnoughMoneyException();
    }

    balance -= drink.getPrice();
    return drink;
  }
}
