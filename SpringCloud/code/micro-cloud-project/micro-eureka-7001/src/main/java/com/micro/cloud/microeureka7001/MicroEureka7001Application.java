package com.micro.cloud.microeureka7001;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.server.EnableEurekaServer;

@SpringBootApplication
@EnableEurekaServer
public class MicroEureka7001Application {
	public static void main(String[] args) {
		SpringApplication.run(MicroEureka7001Application.class, args);
	}
}
