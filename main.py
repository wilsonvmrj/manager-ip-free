from fasthtml.common import *


app,rt = fast_app(live=True)


@rt('/')
def get(): 
  return Titled("Manager IPs", 
                
                Body(
                  Header(
                    
                      H2("Tabela de ips"),
                      Search(
                        Input(type="search"),
                        Button("Search"),
                        target_id="ip-tables",
                        hx_select="ip-tables",
                      )
                                      

                  ),
                  Div(
                    Table(
                      Thead(
                        Th('VLAN'),
                        Th('NETWORKING'),
                        Th('IP'),
                        Th('NOME SERVIDOR'),
                        Th('STATUS'),                     
                      ),
                      Tbody(
                        Tr(
                          Th("505"),
                          Td("10.236.5.0/24"),
                          Td("10.236.5.29"),
                          Td("VSH-NGINX-SERVER"),
                          Td("ok"),                      
                        ),
                            
                        Tr(
                          Th("505"),
                          Td("10.236.5.0/24"),
                          Td("10.236.5.30"),
                          Td("VSH-MSSQL-SERVER"),
                          Td("ok"),                      
                        ),
                        Tr(
                          Th("505"),
                          Td("10.236.5.0/24"),
                          Td("10.236.5.31"),
                          Td("VSH-MSSQL-SERVER"),
                          Td("ok"),                      
                        ),
                      ),
                      cls="striped",
                      id="ip-tables"

                    )
                ),  )
          )



serve()


