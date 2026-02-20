
import logging

# Configure logging to show time, level, and message
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_total_discount(category, tier):
    """
    Returns the total discount percentage based on product category
    and discount tier level.
    """

    # Base discount percentages by category
    category_rates = {
        "Electronics": 10,
        "Clothing": 15,
        "Books": 5,
        "Home": 12
    }

    # Additional discount percentages by tier
    tier_rates = {
        "Premium": 5,
        "Standard": 0,
        "Budget": 2
    }

    # Get discount values (default to 0 if not found)
    cat_discount = category_rates.get(category, 0)
    tier_discount = tier_rates.get(tier, 0)

    return cat_discount + tier_discount


def process_products(input_file, output_file):
    """
    Reads product data, calculates final prices,
    and writes a formatted pricing report.
    """

    try:
        product_list = []
        total_discount_percent = 0

        # Open and read input file
        with open(input_file, "r") as file:
            for line_number, line in enumerate(file, 1):
                try:
                    # Split each line into components
                    name, price_str, category, tier = line.strip().split(",")

                    # Convert price string into float
                    base_price = float(price_str)

                    # Calculate total discount percentage
                    discount_percent = get_total_discount(category, tier)

                    # Calculate discount amount and final price
                    discount_value = base_price * (discount_percent / 100)
                    final_price = base_price - discount_value

                    # Store product details in dictionary
                    product_list.append({
                        "name": name,
                        "base": base_price,
                        "discount_percent": discount_percent,
                        "discount_value": discount_value,
                        "final": final_price
                    })

                    total_discount_percent += discount_percent

                except ValueError:
                    logging.error(f"Line {line_number}: Invalid price format")
                    continue

        # Write formatted pricing report
        with open(output_file, "w") as report:

            # Write header section
            report.write("=" * 80 + "\n")
            report.write("PRODUCT PRICING REPORT\n")
            report.write("=" * 80 + "\n")
            report.write(f"{'Product Name':<30}{'Base Price':>12}{'Disc %':>10}"
                         f"{'Disc $':>12}{'Final Price':>14}\n")
            report.write("-" * 80 + "\n")

            # Write each product's pricing details
            for item in product_list:
                report.write(f"{item['name']:<30}"
                             f"${item['base']:>11.2f}"
                             f"{item['discount_percent']:>9.1f}%"
                             f"${item['discount_value']:>11.2f}"
                             f"${item['final']:>13.2f}\n")

            report.write("=" * 80 + "\n")

        # Print summary to console
        avg_discount = (total_discount_percent / len(product_list)) if product_list else 0

        print("\nProcessing Complete!")
        print(f"Total products processed: {len(product_list)}")
        print(f"Average discount applied: {avg_discount:.2f}%")
        print(f"Report saved as: {output_file}")

        logging.info("Pricing report generated successfully.")

    except FileNotFoundError:
        logging.error("Input file not found.")
        print(f"Error: The file '{input_file}' does not exist.")

    except PermissionError:
        logging.error("Permission denied when writing output file.")
        print(f"Error: Cannot write to '{output_file}'.")

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"Unexpected error: {e}")


# Run the program
if __name__ == "__main__":
    process_products("products.txt", "pricing_report.txt")
