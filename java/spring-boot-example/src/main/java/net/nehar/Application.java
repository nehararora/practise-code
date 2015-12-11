package net.nehar;

/**
 * Created by nehar on 12/11/15.
 */

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;

// logging imports
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.util.Arrays;

@SpringBootApplication
public class Application {



    public static void main(String[] args){
        final Logger logger = LogManager.getLogger(Application.class);

        ApplicationContext ctx = SpringApplication.run(Application.class, args);

        String[] beans = ctx.getBeanDefinitionNames();
        Arrays.sort(beans);
        for (String bean: beans){
            logger.debug("Bean: "+ bean);
        }
    }
}
