def encode(args):
    from ..service import EncoderService
    with EncoderService(args) as es:
        es.join()


def index(args):
    from ..service import IndexerService
    with IndexerService(args) as es:
        es.join()


def client(args):
    from ..service import ClientService

    with ClientService(args) as cs:
        data = [v for v in args.txt_file if v.strip()]
        if not data:
            raise ValueError('input text file is empty, nothing to do')
        else:
            result = cs.query(data)
            if result:
                print(type(result))
                print(result.client_id)
                print(result.req_id)
                print(result.content_type)
                print(result.msg_type)
                print(type(result.msg_content))
        cs.join()