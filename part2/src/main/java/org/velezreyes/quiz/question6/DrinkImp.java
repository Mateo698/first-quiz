package org.velezreyes.quiz.question6;

public class DrinkImp implements Drink {
  private String name;
  private int price;
  private boolean isFizzy;

  public DrinkImp(String name, int price, boolean isFizzy) {
    this.name = name;
    this.price = price;
    this.isFizzy = isFizzy;
  }

  @Override
  public String getName() {
    return name;
  }

  public int getPrice() {
    return price;
  }

  @Override
  public boolean isFizzy() {
    return isFizzy;
  }
}
