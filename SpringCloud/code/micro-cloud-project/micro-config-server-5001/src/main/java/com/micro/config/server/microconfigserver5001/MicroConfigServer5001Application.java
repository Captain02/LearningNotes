package com.micro.config.server.microconfigserver5001;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.cloud.config.server.EnableConfigServer;
import org.springframework.cloud.netflix.eureka.EnableEurekaClient;

@SpringBootApplication
@EnableEurekaClient
@EnableConfigServer
public class MicroConfigServer5001Application {

	public static void main(String[] args) {
		SpringApplication.run(MicroConfigServer5001Application.class, args);
	}

}
