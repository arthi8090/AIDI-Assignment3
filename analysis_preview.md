# Analysis Preview

## 1) Statistical question for Part 2
I plan to test whether average daily Bitcoin returns are different on **Fear** days compared to **Greed** days.

## 2) Outcome variable
The main outcome variable is `btc_daily_return`, which is a continuous numeric column showing the percentage change in Bitcoin closing price from one day to the next.

## 3) Grouping variable
The grouping variable is `fear_greed_label_group`, where sentiment labels are grouped into broader categories such as `Fear`, `Greed`, and `Neutral`.

## 4) Binary variable created
I created `positive_return`, which equals 1 when the daily Bitcoin return is greater than 0 and 0 otherwise. This binary variable is useful for a later proportion z-test because it lets me compare the share of positive-return days across sentiment groups.

## 5) Null and alternative hypotheses
- **Null hypothesis (H0):** The mean daily Bitcoin return is the same on Fear days and Greed days.
- **Alternative hypothesis (H1):** The mean daily Bitcoin return is different on Fear days and Greed days.

For the binary outcome:
- **Null hypothesis (H0):** The proportion of positive-return days is the same on Fear days and Greed days.
- **Alternative hypothesis (H1):** The proportion of positive-return days is different on Fear days and Greed days.

## 6) Best-fitting test
A **two-sample t-test** fits the first question because `btc_daily_return` is continuous and the comparison is between two sentiment groups. A **two-proportion z-test** would fit the second question because `positive_return` is binary and can be compared across Fear and Greed days.
