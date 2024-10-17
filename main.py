from fasthtml.common import *


app,rt = fast_app(live=True)


@rt('/')
def get(): 
  return Body(
                Header(
                  H1("Teste")
                ),                
                Div(
                 Table(
                   Thead(
                     Th('VLAN'),
                     Th('NETWORKING'),
                     Th('IP'),
                     Th('STATUS'),                     
                   ),
                   Tbody(
                     Tr(
                       Th("505"),
                       Td("10.236.5.0/24"),
                       Td("10.236.5.29"),
                       Td("ok"),                      
                     ),
                     Tr(
                       Th("505"),
                       Td("10.236.5.0/24"),
                       Td("10.236.5.30"),
                       Td("ok"),                      
                     ),
                     Tr(
                       Th("505"),
                       Td("10.236.5.0/24"),
                       Td("10.236.5.31"),
                       Td("ok"),                      
                     ),
                     
                   )
                 )
                ),  
          )



serve()


