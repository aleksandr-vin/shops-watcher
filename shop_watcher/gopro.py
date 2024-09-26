# -*- coding: utf-8 -*-

import sys
import json
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import typer
from typing_extensions import Annotated
from rich import print

app = typer.Typer()

@app.command()
def check(
  products: Annotated[str, typer.Argument(envvar="GOPRO_SHOP_ITEMS", help="Shop products space separated (should contain id, like AEWAL-011, per item)")] = """
https://gopro.com/en/nl/shop/mounts-accessories/ultra-wide-lens-mod/AEWAL-001.html
https://gopro.com/en/nl/shop/mounts-accessories/macro-lens-mod/AEWAL-021.html
https://gopro.com/en/nl/shop/mounts-accessories/anamorphic-lens-mod/AEWAL-011.html
https://gopro.com/en/nl/shop/mounts-accessories/latch-mount-magnetic-hero13/AEMAG-001.html
https://gopro.com/en/nl/shop/mounts-accessories/magnetic-door-power-cable/ADCON-001.html
https://gopro.com/en/nl/shop/mounts-accessories/sports-kit/AKTAC-001.html
https://gopro.com/en/nl/shop/mounts-accessories/jaws/ACMPM-001.html
https://gopro.com/en/nl/shop/mounts-accessories/floaty-floating-camera-case/ADFLT-001.html
https://gopro.com/en/nl/shop/mounts-accessories/polarpro-divemaster-filter-kit-protective-housing/APPRO-006.html
https://gopro.com/en/nl/shop/mounts-accessories/anti-fog-inserts/AHDAF-302.html
https://gopro.com/en/nl/shop/mounts-accessories/the-tool/ATSWR-301.html
"""
):
  """
  Query gopro shop current products state and print availability based on the requested products list
  """
  transport = AIOHTTPTransport(
    url="https://gopro.com/graphql",
    headers={
      'Accept-Language': 'en-GB,en;q=0.9',
      'Location': 'nl',
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15',
      'language': 'en',
    },
  )
  client = Client(transport=transport, fetch_schema_from_transport=False)

  query = gql("""
    query Products($cgid: String!, $offset: Int, $limit: Int, $sort: String, $query: String, $htype: [String], $refinements: [Refinement]) {
      products(
        filters: {cgid: $cgid, offset: $offset, limit: $limit, sort: $sort, query: $query, htype: $htype, refinements: $refinements}
      ) {
        total
        limit
        offset
        products {
          id
          name
          category
          masterId
          customAttributes
          saleInfo {
            salesPrice
            status
          }
          subscriberPrice {
            salesPrice
          }
        }
      }
    }
  """)

  params = {
    "cgid":"mounts-accessories",
    "query":"",
    "offset":0,
    "limit":100,
    "sort":"price_desc",
    "refinements":[
      {"refinementName":"c_compatibility","refinementValues":["HERO13 Black"]}
    ]
  }

  result = client.execute(query, variable_values=params)
  # print(result)

  # {
  #   'id': 'AHDAF-303',
  #   'name': 'Anti-Fog Inserts',
  #   'category': 'Mounts + Accessories',
  #   'masterId': 'AHDAF-303',
  #   'customAttributes': {'c_compatibility': ['HERO13 Black', 'HERO12 Black', 'HERO11 Black', 'HERO11 Black Mini', 'HERO10 Black', 'HERO9 Black', 'HERO8 Black', 'HERO7 Black', 'HERO (2018)', 'HERO6 Black', 'HERO5 Black'],
  #                        'c_productPageUrl': '/shop/mounts-accessories/anti-fog-inserts/AHDAF-302.html',
  #                        'c_customCallout': None},
  #   'saleInfo': {'salesPrice': '€29.99', 'status': 'ORDERABLE'},
  #   'subscriberPrice': {'salesPrice': '€14.99'}
  # }

  for p in result['products']['products']:
    if p['id'] in products:
      if p['saleInfo']['status'] == 'ORDERABLE':
        print(f"[bold][red]{p['saleInfo']['status']}[/red] - {p['name']} - {p['subscriberPrice']['salesPrice']}[/]", file=sys.stdout)
      else:
        print(f"[yellow]{p['saleInfo']['status']}[/] - {p['name']} - {p['subscriberPrice']['salesPrice']}", file=sys.stderr)


if __name__ == "__main__":
  app()