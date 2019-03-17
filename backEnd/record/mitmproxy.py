

        flow.request.headers['User-Agent'] = 'MitmProxy'

        ctx.log.info(str(flow.request.headers))


        print(str(flow.request))