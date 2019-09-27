package com.micro.hystrix.microproviderhystrix8003.dept.dao;

import com.entity.Dept;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;


@Mapper
public interface DeptDao {
    List<Dept> selectlist();
}
