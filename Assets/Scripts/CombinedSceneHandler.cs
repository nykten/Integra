using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.EventSystems;
using UnityEngine.UI;
using Valve.VR.Extras;

public class CombinedSceneHandler : MonoBehaviour
{
    [SerializeField] controllerRemap leftRemap;
    [SerializeField] controllerRemap rightRemap;
    [SerializeField] GameObject remap;
    [SerializeField] GameObject menu;
    

    void Start(){
        
    }

    void Awake()
    {

    }

    public void leaveRemap(){
        remap.SetActive(false);
        menu.SetActive(true);
    }

    public void enterXRemap(){
        remap.SetActive(true);
        menu.SetActive(false);
        leftRemap.scaleXAndY = false;
        rightRemap.scaleXAndY = false;
    }

    public void enterXYRemap(){
        remap.SetActive(true);
        menu.SetActive(false);
        leftRemap.scaleXAndY = true;
        rightRemap.scaleXAndY = true;
    }
    
}