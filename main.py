from data_acquisition.openbb_data import get_stock_data

def main():
    data = get_stock_data("AAPL")
    print(data.head())

if __name__ == "__main__":
    main()
