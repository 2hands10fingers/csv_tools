import csv
import os
import datetime
import time
import shutil

print("\nEATZI'S ITEM NUMER BOT INITIATED\n\n")

def error(inital_statement, time_amt):
  print( '\n' + '- - ' * 12)
  print('\t\t ERROR')
  print(f'\n\t{inital_statement}. \n\t\tPlease try again.\n')
  print('- - ' * 12)
  time.sleep(time_amt)

files = [i  for i in os.listdir('.') if i.endswith('.csv')]
complete_files_list = []

if not files:
  raise SystemExit(f"No CSV Files were found. Make sure you are using the correct directory.\n\t Current Directory: '{os.path.basename(os.getcwd())}'")

while files:

  for num, file in enumerate(files):
    print(f'{num}: {file}')

  blah = input("""
Enter a number for the desired file
Enter ALL for all listed files
Enter DONE to complete the selection
Enter CANCEL to stop opreation


Enter here: """)
  blah = blah.lower()

  if blah == 'done':
    if not complete_files_list:
      error('No files were added to the list', 2)
    else:
      break
  elif blah in ['cancel','quit']:
    os.system('clear')
    raise SystemExit('\nOperation canceled. No files were altered.')
  elif blah == "all":
    for file in files: complete_files_list.append(file)
    break
  else:
    try:
      complete_files_list.append(files[int(blah)])
      del files[int(blah)]
    except IndexError:
      error('That NUMBER is not available', 2)
    except ValueError:
      error('I did not recognize that COMMAND', 2)

  os.system('clear')
  print(f'\nSelected Files: {complete_files_list}\n')


for location in complete_files_list:

  kitchen, pastry, bread, wine, gifts, tamales, elseer = [], [], [], [], [], [], []

  print(f"\nOpening {location}")

  with open(location, 'r') as file:
    csv_reader = list(csv.reader(file))

    desired_columns = {
        "item_sku": None,
        "item_name": None,
        "item_quantity": None,
        "item_refunded_qty": None
      }

    for num, row in enumerate(csv_reader):

      if num == 0:

        for num, column_name in enumerate(row):

          if column_name in ['item_sku','item_name',
                     'item_quantity','item_refunded_qty']:

            desired_columns[column_name] = num

        continue

    for num, row in enumerate(csv_reader):

      if num == 0: continue


      a_category, a_name, a_qty, a_refunded_qty = (desired_columns["item_sku"],
                             desired_columns["item_name"],
                             desired_columns['item_quantity'],
                             desired_columns["item_refunded_qty"])
      line_item = None
      try:
        line_item = {
                "quantity": int(row[a_qty]) + int(row[a_refunded_qty].replace("'", "")),
                "item_name": row[a_name],
                "category": row[a_category]
              }
      except TypeError:
        error('ERROR: Operation canceled. No files were generated.', 2)
        raise SystemExit(f"Something is not right about this file: '{location}'. Check column names.")


      category = line_item["category"]

      if category.startswith('kitchen'):
        kitchen.append(line_item)
      elif category.startswith('pastry'):
        pastry.append(line_item)
      elif category.startswith('bread'):
        bread.append(line_item)
      elif category.startswith('wine'):
        wine.append(line_item)
      elif category.startswith('gifts'):
        gifts.append(line_item)
      elif category.startswith('tamales'):
        tamales.append(line_item)
      else:
        elseer.append(line_item)

  if len(elseer) > 0:
    SystemExit(f'{location}: {elseer}')


  def items_list(the_list):
    items = {}

    for i in the_list:
      item_name = i["item_name"]
      quantity = i["quantity"]
      item_key = items.get(item_name, item_name)

      if item_key == item_name:
        items[item_name] = quantity

      if item_key != item_name:
        items[item_name] = items[item_name] + quantity

    return items

  categories = [
          items_list(kitchen),
          items_list(bread),
          items_list(pastry),
          items_list(gifts),
          items_list(wine),
          items_list(tamales)
         ]

  with open(f'new-{location}', 'w') as write_file:
    writer = csv.writer(write_file)

    print(f"\nProducing {location}\n")
    print("- - " * 10)

    def column_names(category):
      if category == 'Kitchen':
        return writer.writerow([category, "Item Name", "Quantity"])
      return writer.writerow([category, "", ""])

    for count, category in enumerate(categories):

      if count == 0:
        column_names('Kitchen')
      if count == 1:
        column_names('Bread')
      if count == 2:
        column_names('Pastry')
      if count == 3:
        column_names('Gifts')
      if count == 4:
        column_names('Wine')
      if count == 5:
        column_names('Tamales')


      for key, value in sorted(category.items()):
        writer.writerow(["", key, value])

os.system('clear')
current = str(datetime.datetime.now()).replace(':', '_').replace(' ', '_').replace('.', '_')
os.mkdir(current)

for oldfile in map(lambda file: f'new-{file}', complete_files_list):
  shutil.move(oldfile, f'{current}/{oldfile}')

print(f'Successfully Moved Files:\n')
for file in complete_files_list:
  print(f'\t{file}')

print(f'\nFiles are located in: {current}')
