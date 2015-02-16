/**
 *
 * EchoResource.java *
 */
package net.codeses.service;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

@Path("/echo")
public class EchoResource {
    
    @GET
    public String echoBack(){
        return "<html><title></title> <body><h1>Hello back you</h1></body></html>";
        
    }
}
