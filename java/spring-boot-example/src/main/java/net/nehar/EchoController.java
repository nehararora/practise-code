package net.nehar;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;


@RestController
public class EchoController {

    private final static Logger logger = LogManager.getLogger(EchoController.class);

    @RequestMapping("/")
    public String index(){

        logger.debug("I shall greets!");
        return "Greets woild!";
    }
}
