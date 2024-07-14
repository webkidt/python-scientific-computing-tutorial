def arithmetic_arranger(problems, show_answers=False):
  first_list = []
  operator_list = []
  second_list = []
  top_row = ''
  down_row = ''
  dash_row = ''
  sum_row = ''

  def get_longer_details(x, y):
    space_to_add = None
    top_is_longer = None
    llen = None
    if len(x) >= len(y):
      top_is_longer = True
      space_to_add = len(x) - len(y)
      llen = len(x)
    else:
      top_is_longer = False
      space_to_add = len(y) - len(x)
      llen = len(y)
    return [top_is_longer, space_to_add, llen]

  def get_formatted_lists(topList, downList, opList):
    top_formatted_list = []
    down_formatted_list = []
    dash_list = []
    sum_formatted_list = [] if show_answers else None

    for i, j, k in zip(topList, downList, opList):
      top_operand_is_longer, space_added_to_operator, longest_len = get_longer_details(
          i, j)

      if top_operand_is_longer:
        op_space = space_added_to_operator + 1
        long_space = ' ' * op_space
        op = k + long_space
        sec = op + j
        down_formatted_list.append(sec)
        sp = ' ' * 2
        top = sp + i
        top_formatted_list.append(top)
      else:
        new_space = space_added_to_operator + 2
        long_space = ' ' * new_space
        top = long_space + i
        top_formatted_list.append(top)
        sec = k + ' ' + j
        down_formatted_list.append(sec)

      dash_len = longest_len + 2
      d = '-' * dash_len
      dash_list.append(d)

      if sum_formatted_list is not None:
        ans = None
        if k == '+':
          ans = int(i) + int(j)
        if k == '-':
          ans = int(i) - int(j)
        sum_string = str(ans)
        sum_len = len(sum_string)
        space_before = 2
        if sum_len > longest_len:
          dif = sum_len - longest_len
          space_before -= dif
        if sum_len < longest_len:
          dif = longest_len - sum_len
          space_before += dif
        sum_space = ' ' * space_before
        formatted_sum = sum_space + sum_string
        sum_formatted_list.append(formatted_sum)

    return [top_formatted_list, down_formatted_list, dash_list, sum_formatted_list] if show_answers else [top_formatted_list, down_formatted_list, dash_list]

  if problems and len(problems) <= 5:
    for el in problems:
      if '+' in el:
        l = el.split('+')
        a = l[0].strip()
        b = l[1].strip()
        if a.isdigit() and b.isdigit():
          if len(a) < 5 and len(b) < 5:
            first_list.append(a)
            second_list.append(b)
            operator_list.append('+')
          else:
            return 'Error: Numbers cannot be more than four digits.'
        else:
          return 'Error: Numbers must only contain digits.'
      elif '-' in el:
        l = el.split('-')
        a = l[0].strip()
        b = l[1].strip()
        if a.isdigit() and b.isdigit():
          if len(a) < 5 and len(b) < 5:
            first_list.append(a)
            second_list.append(b)
            operator_list.append('-')
          else:
            return 'Error: Numbers cannot be more than four digits.'
        else:
          return 'Error: Numbers must only contain digits.'
      else:
        return "Error: Operator must be '+' or '-'."
  else:
    return 'Error: Too many problems.'

  if show_answers:
    tList, dList, dashList, sumList = get_formatted_lists(
        first_list, second_list, operator_list)
    zipped = zip(tList, dList, dashList, sumList)

    for i, (a, b, c, d) in enumerate(zipped):
      row_space = ' ' * 4
      if i == len(tList) - 1:
        top_row += a
        down_row += b
        dash_row += c
        sum_row += d
      else:
        top_row += a + row_space
        down_row += b + row_space
        dash_row += c + row_space
        sum_row += d + row_space
  else:
    tList, dList, dashList = get_formatted_lists(
        first_list, second_list, operator_list)
    zipped = zip(tList, dList, dashList)

    for i, (a, b, c) in enumerate(zipped):
      row_space = ' ' * 4
      if i == len(tList) - 1:
        top_row += a
        down_row += b
        dash_row += c
      else:
        top_row += a + row_space
        down_row += b + row_space
        dash_row += c + row_space

  formatted_problems = top_row + '\n' + down_row + '\n' + \
      dash_row + ('\n' + sum_row if show_answers else '')

  return formatted_problems


print(f'\n{arithmetic_arranger(
  ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}')
