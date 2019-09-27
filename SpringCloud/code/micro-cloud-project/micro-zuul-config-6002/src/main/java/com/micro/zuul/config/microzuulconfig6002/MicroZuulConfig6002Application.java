package com.micro.zuul.config.microzuulconfig6002;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.zuul.EnableZuulProxy;
import org.springframework.cloud.netflix.zuul.EnableZuulServer;

@SpringBootApplication
@EnableZuulProxy
public class MicroZuulConfig6002Application {

	public static void main(String[] args) {
		SpringApplication.run(MicroZuulConfig6002Application.class, args);
	}

}
