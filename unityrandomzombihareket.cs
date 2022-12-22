using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;

public class Zombi : MonoBehaviour
{
    private Vector3 randomPos;

    private GameObject target;
    private NavMeshAgent agent;
    private Animator anim;
    private bool isRunning;

    private bool isWalking;

    private void Start()
    {
        randomPos = transform.position;
        target = GameObject.FindWithTag("Player");
        agent = GetComponent<NavMeshAgent>();
        anim = GetComponent<Animator>();


    }
    private void Update()
    {
        if (Vector3.Distance(transform.position, target.transform.position) <= 5) 
        {
            ChasePlayer();
        }
        else if(isRunning)
        {
            WalkToRandomSpot();
        }
        if (isWalking)
        {
            if (Vector3.Distance(transform.position, randomPos) <= 1)
            {
                WalkToRandomSpot();
            }
        }
        
        
        private void ChasePlayer()
    {
        agent.SetDestination(target.transform.position);
        if (!isRunning)
        {
            isRunning = true;
            isWalking = false;
            agent.speed = 3.5f;
            //trigger animations
        }

    }
    private void WalkToRandomSpot()
    {
        agent.speed = 0.75f;
        randomPos = MapManager.instance.GetRandomPos();

        agent.SetDestination(randomPos);

        isRunning = false;
        isWalking = true;
        // Animations
    }
        
        
    }
