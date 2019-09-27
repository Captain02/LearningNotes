package com.micro.eureka.microeurekaconfig7002;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.config.server.EnableConfigServer;
import org.springframework.cloud.netflix.eureka.EnableEurekaClient;

@SpringBootApplication
@EnableConfigServer
public class MicroEurekaConfig7002Application {

	public static void main(String[] args) {
		SpringApplication.run(MicroEurekaConfig7002Application.class, args);
	}

}
