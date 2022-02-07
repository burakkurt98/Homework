class WebPush:
    platform = ""
    optin = False
    global_Frequency_capping = ""
    start_date = ""
    end_date = ""
    language = ""
    push_type = ""

    def __init__(self):
        pass

    def send_push(self):
        print("Push Gonderildi")


class TriggerPush(WebPush):
    trigger_page = ""

    def __init__(self):
        WebPush.__init__(self)


class BulkPush(WebPush):
    send_date = 0

    def __init__(self):
        WebPush.__init__(self)


class SegmentPush(WebPush):
    segment_name = ""

    def __init__(self):
        WebPush.__init__(self)


class PriceAlertPush(WebPush):
    price_info = 0
    discount_rate = 0.0

    def __init__(self):
        WebPush.__init__(self)

    def discount_price(self, price_info, discount_rate):
        self.price_info = price_info
        self.discount_rate = discount_rate
        return self.price_info / self.discount_rate


class InstockPush(WebPush):
    stock_info = False

    def __init__(self):
        WebPush.__init__(self)

    def stock_update(self):
        self.stock_info = not self.stock_info
        return self.stock_info


def main():
    web_push_object = WebPush()
    trigger_push_object = TriggerPush()
    bulk_push_object = BulkPush
    segment_push_object = SegmentPush()
    price_alert_push_object = PriceAlertPush()
    instock_push_object = InstockPush()
    web_push_object.send_push()
    discount_price = price_alert_push_object.discount_price(1000, 15)
    print(discount_price)
    stock_update = instock_push_object.stock_update()
    print(stock_update)
    stock_update = instock_push_object.stock_update()
    print(stock_update)


if __name__ == '__main__':
    main()
