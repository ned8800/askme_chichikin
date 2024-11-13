def paginations_params(page_num, paginator, page):
    plusTwoPages = page_num + 2
    substractTwoPages = page_num - 2
    try:
        leftArrowBorder = paginator.page(substractTwoPages)
        leftArrow = True
    except:
        leftArrow = False
        leftArrowBorder = None

    try:
        rightArrowBorder = paginator.page(plusTwoPages)
        rightArrow = True
    except:
        rightArrow = False
        rightArrowBorder = None

    flagFirstPage = True if page.number <= 1 else False
    flagLastPage = True if page.number == paginator.num_pages else False

    params = {
        'left_switch': leftArrow,
        'right_switch': rightArrow,
        'is_first_page': flagFirstPage,
        'is_last_page': flagLastPage,
        'arrows_left_border': leftArrowBorder,
        'arrows_right_border': rightArrowBorder,
        'two_pages_ahead': plusTwoPages,
        'two_pages_behind': substractTwoPages,
    }

    return params