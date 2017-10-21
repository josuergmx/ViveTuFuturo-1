package com.project.vive.repository;

import java.io.Serializable;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.project.vive.entity.Login;

@Repository("loginRepository")
public interface LoginRepository extends JpaRepository<Login, Serializable>{
	public abstract Login findById(String id);
}
